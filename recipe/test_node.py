from altair_saver import NodeSaver

spec = {"data": {"values": []}, "mark": "point"}
out = NodeSaver(spec).mimebundle('png')
assert "image/png" in out
