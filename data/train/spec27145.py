import numpy as np 

def function(x):

	v3 = 0
	b1 = x
	paths = []
	try:
		if b1 >= 1:
			x = x*8
			v3 = v3-5
			v3 = v3-2
			paths.append(1)
		else:
			x = x/3
			v3 = v3*3
			paths.append(2)
		if b1 < 2:
			x = 1/2
			paths.append(3)
		else:
			v3 = 8+b1
			b1 = 5-b1
			v3 = v3*v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))