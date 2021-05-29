import numpy as np 

def function(x):

	v5 = 3
	r6 = x
	x = x
	paths = []
	try:
		if v5 <= 2:
			x = 3-x
			paths.append(1)
		else:
			v5 = r6*3
			paths.append(2)
		if v5 > 9:
			v5 = v5*3
			x = 6*v5
			paths.append(3)
		else:
			v5 = v5/2
			v5 = r6/8
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))