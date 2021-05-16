import Foundation
import App

# Usually, you need only edit these seven lines
abbrev = 'Example'					# Short name, no spaces, used as a preface for descriptions
iconName = 'Example'				# Name of icon .tga file
longName = 'Example'				# Long name with spaces
shipFile = 'Example'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Other Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Other Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_VORCHA		# I'm not sure how important this is.

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'Example',			# The full name of your mod if applicable
	'author': 'John Doe',					# Your name here
	'version': '1.0',						# No more than one period please!
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],				# Source for this mod
	'comments': ''						# General info
}

########################################################################
# Uncomment (remove the # symbol and space from) the line which has a ShipDef
# you want.  A generic ship should use ShipDef.  If you want a Federation Ship
# put a # in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.Example = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.CardStarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.KlingonShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.KessokShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.FerengiShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
# Foundation.ShipDef.Example = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Example.desc = 'Yackety schmackety.'

########################################################################
# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:			Foundation.ShipDef.Example.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.Example.RegisterQBPlayerShipMenu(playerMenuGroup)
