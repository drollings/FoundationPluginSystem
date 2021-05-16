Foundation plugin system for Bridge Commander

Beta release, March 20, 2002

Written by Daniel B. Houghton (aka Dasher42), 2002.  All rights reserved.


By default, Bridge Commander allows a great deal of moddability, but adding new ships
requires users to download the SDK and edit the .py files.  This is a tedious process,
and it is unfeasible to distribute, say, an edited QuickBattle.py for every ship out 
there.

This is a system to allow easy integration of new ships into Bridge Commander.
It replaces the static indexes of Bridge Commander with dynamic structures, thus 
providing the means for ship modders to easily distribute their ships without
overwriting any of the end user's files.

To add a ship with this system, you merely copy in the ship, copy its plugin .py file
into the Plugins folder, and edit Plugins\Plugins.py to import the new ship.  That's it!
No more plumbing the depths of QuickBattle.py.

Ship modders:  You need only include this plugins file, an example of which is given as
Plugins\Examples.py.  Even creating this is far easier than what stock BC requires.

Enjoy!


------------------------------------------------------

INSTALLATION

To install this, simply copy the files into the Bridge Commander installation - 
or a second copy of it, which I do *strongly* recommend.  This can be done with a 
simple copy of the Bridge Commander folder.  

This package is beta, and has not been tested for compatibility with single player 
and multiplayer game modes.

As a result, you should have:

(Bridge Commander Folder)\Foundation_Readme.txt
(Bridge Commander Folder)\scripts\Foundation.py
(Bridge Commander Folder)\scripts\Registry.py
(Bridge Commander Folder)\scripts\loadspacehelper.pyc
(Bridge Commander Folder)\scripts\Icons\ShipIcons.pyc
(Bridge Commander Folder)\scripts\Plugins\__init__.py
(Bridge Commander Folder)\scripts\Plugins\Neghvar.py
(Bridge Commander Folder)\scripts\Plugins\Plugins.py
(Bridge Commander Folder)\scripts\Plugins\StaticDefs.py
(Bridge Commander Folder)\scripts\Tactical\Interface\ShieldsDisplay.pyc
(Bridge Commander Folder)\scripts\Tactical\Interface\WeaponsDisplay.pyc

where (Bridge Commander Folder) is wherever the new copy of Bridge Commander is located.

------------------------------------------------------

USAGE

If you're a user that wants to incorporate a plugin-ready ship, copy it into the 
BridgeCommander folders, and add a line to the end of Plugins\Plugins.py.  It should 
look like this:

import ShipName

Instructions are included as comments within that file.  If the ship packages does not 
include a module for the Plugins folder, make a copy of Plugins\Neghvar.py and edit it 
according to the directions below, and update its Scripts\Ships\ShipName.py file.

Got a ship you want to make plugin-ready?  Here is a step-by-step guide to making a ship 
compliant with the Dynamic Plugin.  When done you will have something that you can 
distribute and that the end user can integrate by adding a single import line to their 
Plugins\Plugins.py.

1)  Export the models.  You should have the following:

The model and textures:

Data\Models\Ships\NewShip\
Data\Models\Ships\NewShip\NewShip.NIF (optionally NewShipMed.NIF and NewShipLow.NIF too)
Data\Models\Ships\NewShip\High\(textures as .TGA's)
Data\Models\Ships\NewShip\Medium\(textures as .TGA's)
Data\Models\Ships\NewShip\Low\(textures as .TGA's)

The ship definition and hardpoints:

Scripts\Ships\NewShip.py
Scripts\Ships\Hardpoints\newship.py


2)  Scripts\Ships\NewShip.py must have a properly set up GetShipStats() section for the 
    ship to work.  Some of these parameters are case-sensitive; be careful!  

---
def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/NewShip/NewShip.nif",
		"FilenameMed": "data/Models/Ships/NewShip/NewShipMed.nif",
		"FilenameLow": "data/Models/Ships/NewShip/NewShipLow.nif",
		"Name": "NewShip",			#  <-  These are 
		"HardpointFile": "newship",		#  <-  important!
		"Species": Multiplayer.SpeciesToShip.VORCHA	
		# ^^^^^^ The importance of this is still unknown
	}
	return kShipStats

---


3)  You must make a Plugins\NewShip.py file.  It is important that it refer to the name 
    of the Scripts\Ships\NewShip.py file, and it is case-sensitive.

---
import Foundation
import App


# Just get the name right.  The species doesn't really matter.
Foundation.ShipDef.NewVorcha = Foundation.ShipDef('NewShip', App.SPECIES_GALAXY)
#    Name and case sensitive - this is really important! ^^^^^^^

# What menu group for the ships?
Foundation.ShipDef.NewVorcha.RegisterQBShipMenu('Other Ships')

# What menu group for the player ships?
Foundation.ShipDef.NewVorcha.RegisterQBPlayerShipMenu('Other Ships')
---


4)  Got an icon?  A 128x128 .TGA of your ship?  Put it in Data\Icons\Ships.  
    If its name is different from that of the ship, the Example.py file will 
    show you how to use it.

5)  In order to eliminate the ??? buttons and descriptions, you must use the TGL exporter 
    included with the Bridge Commander SDK.  You need to have strings to match "NewShip" 
    and "NewShip Description".

6)  As a matter of good practice, take the final step that your users will need to take.  
    Edit Plugins\Plugins.py and add this line to the bottom:

---
import NewShip
---

That's it!


------------------------------------------------------

WHAT'S NEW?

March 20, 2002 release:

This version of the mod corrects cases where ship icons would not appear in QuickBattle.
This fix also resolves an issue with plugins that include ships that supercede ships
already included by Bridge Commander or previously loaded plugins.  This should make it
simple to include a revised ship without overwriting the original one (unless you feel it
absolutely necessary).
	
There's still no easy solution to the '???' button issue unless you install TGL's.  This
mod may have a simpler solution, but largely, this problem is out of scope.  Don't worry!
The game will still work!

Multiplayer remains largely untested.  You're likely to see missing ship icons and more.

I've also included a sample plugin file to load DamoclesX's Mod Pack 1.02 if you have it.
If you don't, get it and install it - just DON'T let it overwrite any existing files, 
and don't install the outdated version of this mod that it includes.  I've even included
a line to uncomment in this release's scripts\Plugins\Plugins.py file.


------------------------------------------------------

TROUBLESHOOTING

Did you install this mod and then see Bridge Commander stop working?  Walk through
the following steps:


1)  Is this about the '???' buttons?  They still work.  See the Bridge 
    Commander SDK's documentation about TGL files.  If this is your only 
    problem, relax.  We're working on it. ;)

2)  Did you unpack this into your copy of the Bridge Commander directory?  If so, this 
    file you're reading should appear there, above \data, \scripts, \Screen Shots, 
    everything.  
    
3)  Did you have any mods already installed that could be conflicting?  Try making 
    a fresh install of Bridge Commander into another folder and installing this mod there.
    
4)  Did you install a plugin and then see the game stop working?  Try putting # signs
    in front of every import statement in \scripts\Plugins\Plugins.py except 
    "import StaticDefs".
    
    Did it work?  Maybe an import statement is incorrect.  Double-check to be sure; 
    these things are case-sensitive and must match the .py file's name.  Also, make 
    sure you have no leading spaces; a line that reads " import NewShip.py" is trouble!
    
    If the plugin still doesn't work, it or Foundation itself could have an error, or
    maybe there's a conflict of some kind.
    
5)  Make sure there are no .PY files in your Bridge Commander folder that correspond to 
    the ones included herein.  They could be compiled to .PYCs and break this mod.  
    QuickBattles.py, loadspacehelper.py, ShipIcons.py, ShieldDisplay.py, and 
    WeaponsDisplay.py would be obvious offenders.

6)  Get the latest version of this mod from: 

    www.beldar.com/~dasher/Foundation-current.zip
    
    You might get the fix you so crave.

7)  Did you install another mod after this one that overwrote Foundation?  
    Regrettably, all other existing QuickBattle mods are incompatible with this one 
    as of now.  Work will go forward to make them into plugins as well.  If you want 
    this mod and them, make another fresh copy of Bridge Commander or just get your 
    hands dirty.
    
8)  Failing all this, append " -TestMode" to your Bridge Commander icon's target 
    field, hit the back apostrophe in-game when it starts to have trouble, and press 
    enter.  Tell us what happened.


------------------------------------------------------

NOTE TO DEVELOPERS

This plugin project is meant to expand beyond ships into an easy "glue layer" for 
Bridge Commander mods, providing a simple installation process and an easy way to 
activate or deactivate mods.  As such, please do not distribute modified versions of
the existing .PY and .PYC files in this mod indiscriminately, as you could break 
compatibility with other mods that people *will* try to install and future versions of
Dynamic Tables.  If you really must, just include a scripts\Plugins\Plugins.py file.
This will save trouble for me, you, and the users.


------------------------------------------------------

LEGALESE:

This software is provided as-is, and the author (Daniel B. Houghton) makes 
no guarantee of the performance of this software, its security, compatibility, 
safety, or usefulness, and cannot be held liable for any consequence of this 
software's use.

Permission is given to modify or distribute the acommpanying files as a 
component of Bridge Commander under the terms of the Activision SDK license 
with the following provisions:

1.  This readme file shall be included in any distribution, and credit given in
any work which incorporates this package's files,

2.  Any changes to the .PY files included in this distribution that do not 
incorporate Activision material shall be included as source code per the terms of 
the Lesser GNU Public License (LGPL), where this does not violate the terms of 
the Activision SDK license,

---

In short, use it, hack it, if you distribute changes to it make them open and give 
me credit.  That's all, have fun!


Daniel Houghton AKA Dasher42 
dasher_42@yahoo.com