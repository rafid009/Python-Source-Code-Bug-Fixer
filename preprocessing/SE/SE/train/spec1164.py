import numpy as np 

def function(x):

	q4 = 2
	v3 = 9
	paths = []
	try:
		if v3 <= 7:
			v3 = v3+7
			x = 9+q4
			paths.append(1)
		else:
			v3 = 1-v3
			paths.append(2)
		if q4 >= 5:
			v3 = q4-v3
			q4 = q4-2
			paths.append(3)
		else:
			x = 9+x
			x = x*x
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