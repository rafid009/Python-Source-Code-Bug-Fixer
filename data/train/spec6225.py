import numpy as np 

def function(x):

	a1 = x
	j0 = x
	paths = []
	try:
		if j0 <= 5:
			j0 = x-x
			x = x*0
			j0 = j0-4
			paths.append(1)
		else:
			a1 = 3-a1
			a1 = 5/3
			j0 = a1+a1
			paths.append(2)
		if j0 > 5:
			j0 = j0-5
			paths.append(3)
		else:
			x = x-5
			a1 = a1+9
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))