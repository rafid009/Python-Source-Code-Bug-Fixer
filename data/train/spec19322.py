import numpy as np 

def function(x):

	p5 = 1
	v6 = x
	paths = []
	try:
		if x > 4:
			v6 = v6/x
			v6 = 0+8
			p5 = p5/v6
			paths.append(1)
		else:
			v6 = v6-5
			paths.append(2)
		if x >= 6:
			x = 5+5
			v6 = v6*7
			x = 2*v6
			paths.append(3)
		else:
			x = x-6
			v6 = 1-7
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