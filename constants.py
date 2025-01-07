PUBLIC_ENTRYPOINTS = """```
# These are community-provided public Reticulum entrypoints
# served over TCP, and available over the public Internet.

  [[quad4net tcp]]
    type = TCPClientInterface
    enabled = yes
    target_host = rns.quad4.io
    target_port = 4242

  [[ChaosNet]]
    type = TCPClientInterface
    interface_enabled = True
    target_host = rns.c3.jitter.eu
    target_port = 4242

  [[dismails TCP Interface]]
    type = TCPClientInterface
    interface_enabled = true
    target_host = rns.dismail.de
    target_port = 7822

  [[interloper node]]
    type = TCPClientInterface
    interface_enabled = true
    target_host = intr.cx
    target_port = 4242

  [[The Outpost]]
    type = TCPClientInterface
    interface_enabled = true
    target_host = theoutpost.life
    target_port = 4242

  [[Beleth RNS Hub]]
    type = TCPClientInterface
    interface_enabled = true
    target_host = rns.beleth.net
    target_port = 4242

  [[SparkN0de]]
    type = TCPClientInterface
    interface_enabled = true
    target_host = aspark.uber.space
    target_port = 44860

  [[nisa-node]]
    type = TCPClientInterface
    enabled = yes
    target_host = nisa.cat
    target_port = 4242

  [[acehoss]]
    type = TCPClientInterface
    enabled = yes
    target_host = rns.acehoss.net
    target_port = 4242

  [[RNS Testnet StoppedCold]]
    type = TCPClientInterface
    enabled = yes
    target_host = rns.stoppedcold.com
    target_port = 4242

  [[RNS COMSEC-RD]]
    type = TCPClientInterface
    enabled = yes
    target_host = 80.78.23.249
    target_port = 4242

  [[R-Net TCP]]
    type = TCPClientInterface
    enabled = yes
    target_host = istanbul.reserve.network
    target_port = 9034

  [[RNS TCP Node Germany 001]]
    type = TCPClientInterface
    enabled = true
    target_host = 202.61.243.41
    target_port = 4965

  [[RNS TCP Node Germany 002]]
    type = TCPClientInterface
    enabled = true
    target_host = 193.26.158.230
    target_port = 4965

  [[Quortal TCP Node]]
    type = TCPClientInterface
    enabled = true
    target_host = reticulum.qortal.link
    target_port = 4242

  [[mobilefabrik TCP]]
    type = TCPClientInterface
    enabled = true
    target_host = phantom.mobilefabrik.com
    target_port = 4242

  [[g00n.cloud Hub]]
    type = TCPClientInterface
    enabled = true
    target_host = dfw.us.g00n.cloud
    target_port = 6969

  [[RNS_Transport_US-East]]
    type = TCPClientInterface
    interface_enabled = true
    target_host = 45.77.109.86
    target_port = 4965

  [[Tidudanka.com]]
    type = TCPClientInterface
    enabled = yes
    target_host = 164.90.180.40
    target_port = 37500

```
"""