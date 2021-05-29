import numpy as np 

def function(x):

	a1 = x
	v6 = 5
	paths = []
	try:
		if x < 2:
			a1 = x+1
			x = x+v6
			paths.append(1)
		else:
			a1 = 0/3
			v6 = v6/5
			a1 = a1-9
			paths.append(2)
		if a1 > 6:
			x = x+a1
			x = x/a1
			a1 = a1*2
			paths.append(3)
		else:
			v6 = 5+v6
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))