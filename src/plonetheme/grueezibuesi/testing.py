# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    PLONE_FIXTURE,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import plonetheme.grueezibuesi


class PlonethemeGrueezibuesiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.grueezibuesi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plonetheme.grueezibuesi:default")


PLONETHEME_GRUEEZIBUESI_FIXTURE = PlonethemeGrueezibuesiLayer()


PLONETHEME_GRUEEZIBUESI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_GRUEEZIBUESI_FIXTURE,),
    name="PlonethemeGrueezibuesiLayer:IntegrationTesting",
)


PLONETHEME_GRUEEZIBUESI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_GRUEEZIBUESI_FIXTURE,),
    name="PlonethemeGrueezibuesiLayer:FunctionalTesting",
)


PLONETHEME_GRUEEZIBUESI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_GRUEEZIBUESI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="PlonethemeGrueezibuesiLayer:AcceptanceTesting",
)
