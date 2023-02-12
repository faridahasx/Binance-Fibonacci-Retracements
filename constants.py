API_KEY = "YOUR API KEYS"
API_SECRET = "YOUR SECRET KEYS"

# Total USDT amount to spend for each position
USDT_to_spend = 100

position_limit = 10

# Fibonacci levels
ENTRY_LEVEL = 0.786
EXIT_LEVEL = 0.5


GAIN = 1.2  # 20% gain from open to high


SOCKET = 'wss://stream.binance.com:9443/ws/1inchusdt@kline_1h/aaveusdt@kline_1h/acmusdt@kline_1h/' \
         'adausdt@kline_1h/aionusdt@kline_1h/akrousdt@kline_1h/algousdt@kline_1h/aliceusdt@kline_1h/' \
         'alpacausdt@kline_1h/alphausdt@kline_1h/ankrusdt@kline_1h/antusdt@kline_1h/arusdt@kline_1h/' \
         'ardrusdt@kline_1h/arpausdt@kline_1h/asrusdt@kline_1h/atausdt@kline_1h/atmusdt@kline_1h/' \
         'atomusdt@kline_1h/audusdt@kline_1h/audiousdt@kline_1h/autousdt@kline_1h/avausdt@kline_1h/' \
         'avaxusdt@kline_1h/axsusdt@kline_1h/badgerusdt@kline_1h/bakeusdt@kline_1h/balusdt@kline_1h/' \
         'bandusdt@kline_1h/barusdt@kline_1h/batusdt@kline_1h/bchusdt@kline_1h/beamusdt@kline_1h/' \
         'belusdt@kline_1h/blzusdt@kline_1h/bnbusdt@kline_1h/bntusdt@kline_1h/bondusdt@kline_1h/' \
         'btcusdt@kline_1h/btgusdt@kline_1h/btsusdt@kline_1h/bttusdt@kline_1h/burgerusdt@kline_1h/' \
         'c98usdt@kline_1h/cakeusdt@kline_1h/celousdt@kline_1h/celrusdt@kline_1h/cfxusdt@kline_1h/' \
         'chrusdt@kline_1h/chzusdt@kline_1h/ckbusdt@kline_1h/clvusdt@kline_1h/cocosusdt@kline_1h/' \
         'compusdt@kline_1h/cosusdt@kline_1h/cotiusdt@kline_1h/crvusdt@kline_1h/ctkusdt@kline_1h/' \
         'ctsiusdt@kline_1h/ctxcusdt@kline_1h/cvcusdt@kline_1h/dashusdt@kline_1h/datausdt@kline_1h/' \
         'dcrusdt@kline_1h/degousdt@kline_1h/dentusdt@kline_1h/dexeusdt@kline_1h/dgbusdt@kline_1h/' \
         'diausdt@kline_1h/dntusdt@kline_1h/dockusdt@kline_1h/dodousdt@kline_1h/dogeusdt@kline_1h/' \
         'dotusdt@kline_1h/drepusdt@kline_1h/duskusdt@kline_1h/egldusdt@kline_1h/enjusdt@kline_1h/' \
         'eosusdt@kline_1h/epsusdt@kline_1h/ernusdt@kline_1h/etcusdt@kline_1h/ethusdt@kline_1h/' \
         'farmusdt@kline_1h/fetusdt@kline_1h/filusdt@kline_1h/fiousdt@kline_1h/firousdt@kline_1h/' \
         'fisusdt@kline_1h/flmusdt@kline_1h/flowusdt@kline_1h/forusdt@kline_1h/forthusdt@kline_1h/' \
         'ftmusdt@kline_1h/fttusdt@kline_1h/funusdt@kline_1h/ghstusdt@kline_1h/grtusdt@kline_1h/' \
         'gtcusdt@kline_1h/gtousdt@kline_1h/gxsusdt@kline_1h/hardusdt@kline_1h/hbarusdt@kline_1h/' \
         'hiveusdt@kline_1h/hntusdt@kline_1h/hotusdt@kline_1h/icpusdt@kline_1h/icxusdt@kline_1h/' \
         'injusdt@kline_1h/iostusdt@kline_1h/iotausdt@kline_1h/iotxusdt@kline_1h/irisusdt@kline_1h/' \
         'jstusdt@kline_1h/juvusdt@kline_1h/kavausdt@kline_1h/keepusdt@kline_1h/keyusdt@kline_1h/' \
         'klayusdt@kline_1h/kmdusdt@kline_1h/kncusdt@kline_1h/ksmusdt@kline_1h/linausdt@kline_1h/' \
         'linkusdt@kline_1h/litusdt@kline_1h/lptusdt@kline_1h/lrcusdt@kline_1h/lskusdt@kline_1h/' \
         'ltcusdt@kline_1h/ltousdt@kline_1h/lunausdt@kline_1h/manausdt@kline_1h/maskusdt@kline_1h/' \
         'maticusdt@kline_1h/mblusdt@kline_1h/mboxusdt@kline_1h/mdtusdt@kline_1h/mdxusdt@kline_1h/' \
         'mftusdt@kline_1h/minausdt@kline_1h/mirusdt@kline_1h/mithusdt@kline_1h/mkrusdt@kline_1h/' \
         'mlnusdt@kline_1h/mtlusdt@kline_1h/nanousdt@kline_1h/nbsusdt@kline_1h/nearusdt@kline_1h/' \
         'neousdt@kline_1h/nknusdt@kline_1h/nuusdt@kline_1h/nulsusdt@kline_1h/oceanusdt@kline_1h/' \
         'ogusdt@kline_1h/ognusdt@kline_1h/omusdt@kline_1h/omgusdt@kline_1h/oneusdt@kline_1h/' \
         'ongusdt@kline_1h/ontusdt@kline_1h/ornusdt@kline_1h/oxtusdt@kline_1h/paxgusdt@kline_1h/' \
         'perlusdt@kline_1h/perpusdt@kline_1h/phausdt@kline_1h/pntusdt@kline_1h/polsusdt@kline_1h/' \
         'pondusdt@kline_1h/psgusdt@kline_1h/pundixusdt@kline_1h/qntusdt@kline_1h/qtumusdt@kline_1h/' \
         'quickusdt@kline_1h/rampusdt@kline_1h/rayusdt@kline_1h/reefusdt@kline_1h/renusdt@kline_1h/' \
         'repusdt@kline_1h/requsdt@kline_1h/rifusdt@kline_1h/rlcusdt@kline_1h/roseusdt@kline_1h/' \
         'rsrusdt@kline_1h/runeusdt@kline_1h/rvnusdt@kline_1h/sandusdt@kline_1h/scusdt@kline_1h/' \
         'sfpusdt@kline_1h/shibusdt@kline_1h/sklusdt@kline_1h/slpusdt@kline_1h/snxusdt@kline_1h/' \
         'solusdt@kline_1h/srmusdt@kline_1h/stmxusdt@kline_1h/storjusdt@kline_1h/stptusdt@kline_1h/' \
         'straxusdt@kline_1h/stxusdt@kline_1h/sunusdt@kline_1h/superusdt@kline_1h/sushiusdt@kline_1h/' \
         'sxpusdt@kline_1h/tctusdt@kline_1h/tfuelusdt@kline_1h/thetausdt@kline_1h/tkousdt@kline_1h/' \
         'tlmusdt@kline_1h/tomousdt@kline_1h/tornusdt@kline_1h/trbusdt@kline_1h/troyusdt@kline_1h/' \
         'truusdt@kline_1h/trxusdt@kline_1h/tvkusdt@kline_1h/twtusdt@kline_1h/umausdt@kline_1h/' \
         'unfiusdt@kline_1h/uniusdt@kline_1h/utkusdt@kline_1h/vetusdt@kline_1h/viteusdt@kline_1h/' \
         'vthousdt@kline_1h/wanusdt@kline_1h/wavesusdt@kline_1h/waxpusdt@kline_1h/winusdt@kline_1h/' \
         'wingusdt@kline_1h/wnxmusdt@kline_1h/wrxusdt@kline_1h/wtcusdt@kline_1h/xemusdt@kline_1h/' \
         'xlmusdt@kline_1h/xmrusdt@kline_1h/xrpusdt@kline_1h/xtzusdt@kline_1h/xvgusdt@kline_1h/' \
         'xvsusdt@kline_1h/yfiusdt@kline_1h/yfiiusdt@kline_1h/zecusdt@kline_1h/zenusdt@kline_1h/' \
         'zilusdt@kline_1h/zrxusdt@kline_1h'
