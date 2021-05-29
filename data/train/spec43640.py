import numpy as np 

def function(x):

	j0 = x
	p3 = 2
	paths = []
	try:
		if j0 <= 4:
			x = 3-p3
			j0 = j0/x
			paths.append(1)
		else:
			x = 5/3
			p3 = 5*5
			x = x-9
			paths.append(2)
		if x <= 4:
			p3 = 4/p3
			paths.append(3)
		else:
			p3 = 0-7
			x = x*0
			x = x-5
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))