config set motd configuration status enabled message Blue info Green

config setprop motd message Blue info Green

To disable the standard MOTD
config setprop sshd MotdStatus disabled

To update

signal-event remoteaccess-update

Colours available (only affect text, not background)

White
Blue
Green
LightGreen
Black
Red
LightRed
DarkGray
LightGray
Cyan
LightCyan
Purple
LightPurple
Std (reverts to normal)

Note they are case sensitive. If a colour name is not recognised it should revert to Std


Install cowsay from EPEL ?
add 'users' to how currently logged in users