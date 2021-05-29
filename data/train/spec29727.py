import numpy as np 

def function(x):

	a9 = 6
	j2 = 8
	paths = []
	try:
		if a9 > 7:
			x = 4/a9
			j2 = j2*0
			x = x/7
			paths.append(1)
		else:
			x = x+a9
			x = 1-x
			a9 = 4*9
			paths.append(2)
		if j2 > 6:
			j2 = j2+1
			paths.append(3)
		else:
			j2 = x*5
			a9 = x/a9
			a9 = a9/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))