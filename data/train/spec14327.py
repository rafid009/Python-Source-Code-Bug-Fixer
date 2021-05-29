import numpy as np 

def function(x):

	p4 = x
	j2 = 7
	paths = []
	try:
		if j2 <= 3:
			j2 = j2+j2
			x = j2+x
			x = x-2
			paths.append(1)
		else:
			p4 = x-p4
			p4 = p4*p4
			x = x-7
			paths.append(2)
		if p4 < 0:
			j2 = j2-8
			paths.append(3)
		else:
			x = 9+7
			p4 = p4-7
			x = p4+2
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))