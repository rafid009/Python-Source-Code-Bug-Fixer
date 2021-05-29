import numpy as np 

def function(x):

	v7 = 2
	q3 = x
	paths = []
	try:
		if q3 >= 4:
			q3 = v7-4
			q3 = 1*q3
			paths.append(1)
		else:
			v7 = v7+9
			q3 = 0+q3
			paths.append(2)
		if v7 <= 3:
			x = x/v7
			x = x*3
			paths.append(3)
		else:
			x = x+5
			v7 = x/9
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))