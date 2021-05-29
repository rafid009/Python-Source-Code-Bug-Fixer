import numpy as np 

def function(x):

	e1 = x
	v3 = x
	x = x
	paths = []
	try:
		if e1 <= 8:
			e1 = e1-e1
			paths.append(1)
		else:
			e1 = e1-x
			e1 = 5+e1
			e1 = e1-e1
			paths.append(2)
		if v3 <= 5:
			v3 = v3-8
			x = x/v3
			x = 7-x
			paths.append(3)
		else:
			v3 = 0+x
			e1 = 1-5
			x = x-v3
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