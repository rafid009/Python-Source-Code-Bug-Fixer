import numpy as np 

def function(x):

	p8 = 1
	v9 = 7
	paths = []
	try:
		if p8 <= 7:
			x = x*1
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if v9 > 9:
			v9 = 1/x
			p8 = 4-p8
			paths.append(3)
		else:
			v9 = v9-x
			x = x/1
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))