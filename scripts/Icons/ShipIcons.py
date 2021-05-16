# ShipIcons.py
#
# Load Ship Icons for interface.
# 
#

import App
import DynamicTables

# Function to load LCARS icon group
def LoadShipIcons(ShipIcons = None):
	
	if ShipIcons is None:
		ShipIcons = App.g_kIconManager.CreateIconGroup("ShipIcons")
		# Add LCARS icon group to IconManager
		App.g_kIconManager.AddIconGroup(ShipIcons)
	
	
	# Glass for when no ship is selected
	TextureHandle = ShipIcons.LoadIconTexture('Data/Icons/Bridge/Background/ScreenBlock.tga')
	ShipIcons.SetIconLocation(App.SPECIES_UNKNOWN, TextureHandle, 0, 0, 8, 8)

	# Federation
	#---------------

	# Galaxy
	# TextureHandle = ShipIcons.LoadIconTexture('Data/Icons/Ships/Galaxy.tga')
	# ShipIcons.SetIconLocation(App.SPECIES_GALAXY, TextureHandle, 0, 0, 128, 128)

	for name in DynamicTables.shipList._arrayList:
		shipDef = DynamicTables.shipList[name]
		iconName = 'Data/Icons/Ships/' + shipDef.iconName + '.tga'

		TextureHandle = ShipIcons.LoadIconTexture(iconName)
		ShipIcons.SetIconLocation(shipDef.num, TextureHandle, 0, 0, 128, 128)
