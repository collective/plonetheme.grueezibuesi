# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import plonetheme.gruezibuesi


class PlonethemeGruezibuesiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.gruezibuesi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.gruezibuesi:default')


PLONETHEME_GRUEZIBUESI_FIXTURE = PlonethemeGruezibuesiLayer()


PLONETHEME_GRUEZIBUESI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_GRUEZIBUESI_FIXTURE,),
    name='PlonethemeGruezibuesiLayer:IntegrationTesting',
)


PLONETHEME_GRUEZIBUESI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_GRUEZIBUESI_FIXTURE,),
    name='PlonethemeGruezibuesiLayer:FunctionalTesting',
)


PLONETHEME_GRUEZIBUESI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_GRUEZIBUESI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeGruezibuesiLayer:AcceptanceTesting',
)
