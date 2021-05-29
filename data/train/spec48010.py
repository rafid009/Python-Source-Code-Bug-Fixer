import numpy as np 

def function(x):

	p8 = x
	t4 = x
	paths = []
	try:
		if p8 > 4:
			p8 = t4-p8
			p8 = 9*p8
			t4 = t4+3
			paths.append(1)
		else:
			p8 = p8+4
			t4 = t4-2
			p8 = 0*p8
			paths.append(2)
		if x > 6:
			t4 = 9-x
			paths.append(3)
		else:
			p8 = p8*0
			p8 = p8+p8
			x = 5+t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))