import numpy as np 

def function(x):

	p4 = 7
	v6 = 7
	paths = []
	try:
		if x > 0:
			v6 = v6*3
			paths.append(1)
		else:
			v6 = v6/7
			paths.append(2)
		if x < 6:
			v6 = v6/x
			x = x+3
			p4 = x*p4
			paths.append(3)
		else:
			x = p4-x
			v6 = 3*4
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))