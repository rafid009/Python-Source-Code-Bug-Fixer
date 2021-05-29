import numpy as np 

def function(x):

	a6 = x
	v6 = x
	paths = []
	try:
		if v6 <= 1:
			x = v6+x
			x = x*0
			x = 5-a6
			paths.append(1)
		else:
			x = x-8
			a6 = a6/a6
			x = x*a6
			paths.append(2)
		if x >= 2:
			x = a6/1
			paths.append(3)
		else:
			a6 = a6*6
			v6 = v6+x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		a6 = v6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))