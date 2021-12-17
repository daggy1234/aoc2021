mapping = {
	"0" : "0000",
	"1" : "0001",
	"2" : "0010",
	"3" : "0011",
	"4" : "0100",
	"5" : "0101",
	"6" : "0110",
	"7" : "0111",
	"8" : "1000",
	"9" : "1001",
	"A" : "1010",
	"B" : "1011",
	"C" : "1100",
	"D" : "1101",
	"E" : "1110",
	"F" : "1111"
}

revd = dict([(v,k) for k,v in mapping.items()])

tmap = {
	"0": "+",
	"1": "*",
	"2": "min",
	"3": "max",
	"5": ">",
	"6": "<",
	"7": "="
}

def parse_inp(inp,vsum,evalv,lastop,subvl ,isbin: bool = False):

	if len(inp) <= 6:
		return vsum, subvl, lastop

	if isbin:
		new_b = ""
		for char in inp:
			new_b += mapping[char]
	else:
		new_b = inp
	v = int(revd["0" + new_b[:3]])
	t = (revd["0" + new_b[3:6]])
	vsum += v
	if t == "4":
		sub_parsed = new_b[6:]
		start_ind = 0
		msubv = ""
		for i in range(5,len(sub_parsed) + 1,5):
			subv = sub_parsed[start_ind:i]
			if subv[0] == "0":
				msubv += subv[1:]
				start_ind = i
				break
			else:
				msubv += subv[1:]
				start_ind = i
		subvl.append(int(msubv, base=2))
		if len(sub_parsed[start_ind:]) == 0:
			return vsum,subvl,lastop
		else:
			return parse_inp(sub_parsed[start_ind:],vsum,evalv,lastop, subvl)
	else:
		op = tmap[t]
		print(f"OP len {lastop} {len(lastop)}")
		i = new_b[6]
		if i == "0":
			to_parse = int(new_b[7:22], base=2)
			vsumb,subvlb,lastopa = parse_inp(new_b[22:(22 + to_parse)],vsum,evalv,lastop,subvl)
			lastopa.append(op)
			vsums,suvls,lastopsa =  parse_inp(new_b[(22 + to_parse):],vsumb,evalv,lastopa,subvlb)
		else:
			to_parse = int(new_b[7:18], base=2)
			print(f"OP c len {lastop} {len(lastop)}")
			lastop.append(op)
			vsums,suvls,lastopsa =  parse_inp(new_b[18:],vsum,evalv,lastop,subvl)
		print(lastopsa)
		return vsums,suvls,lastopsa


print(parse_inp("9C0141080250320F1802104A08", 0,0,[], [],isbin=True))
# parse_inp("8A004A801A8002F478")