class cylinder:
    pi = 3.14

    def volume(cy):
        print(((cy.pi*cy.r**2)*cy.h))

    def surface(cy):
        print((cy.pi*cy.r(cy.r+cy.h)))


cy = cylinder()
cy.r = 2
cy.h = 3
cy.volume()
cy.surface()
