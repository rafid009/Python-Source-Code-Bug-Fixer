import numpy as np 

def function(x):

	t3 = 4
	p2 = x
	paths = []
	try:
		if p2 > 9:
			x = x/7
			t3 = t3-x
			paths.append(1)
		else:
			x = 8+x
			p2 = p2*1
			x = p2-x
			paths.append(2)
		if t3 < 4:
			p2 = 5*8
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))