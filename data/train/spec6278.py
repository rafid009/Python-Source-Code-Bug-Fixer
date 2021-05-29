import numpy as np 

def function(x):

	p4 = 5
	v4 = x
	paths = []
	try:
		if p4 < 0:
			v4 = v4-5
			v4 = 4*8
			paths.append(1)
		else:
			p4 = 6-p4
			v4 = 2+v4
			p4 = p4-p4
			paths.append(2)
		if p4 <= 7:
			p4 = p4*0
			v4 = 4/v4
			paths.append(3)
		else:
			x = 9-5
			x = v4+0
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		p4 = v4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))