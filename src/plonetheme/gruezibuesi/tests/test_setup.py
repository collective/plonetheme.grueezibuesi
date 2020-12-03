# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from plonetheme.gruezibuesi.testing import (
    PLONETHEME_GRUEZIBUESI_INTEGRATION_TESTING  # noqa: E501,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plonetheme.gruezibuesi is properly installed."""

    layer = PLONETHEME_GRUEZIBUESI_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.gruezibuesi is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.gruezibuesi'))

    def test_browserlayer(self):
        """Test that IPlonethemeGruezibuesiLayer is registered."""
        from plonetheme.gruezibuesi.interfaces import (
            IPlonethemeGruezibuesiLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPlonethemeGruezibuesiLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_GRUEZIBUESI_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plonetheme.gruezibuesi'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.gruezibuesi is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.gruezibuesi'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeGruezibuesiLayer is removed."""
        from plonetheme.gruezibuesi.interfaces import \
            IPlonethemeGruezibuesiLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPlonethemeGruezibuesiLayer,
            utils.registered_layers())
