import numpy as np 

def function(x):

	j7 = x
	a8 = 3
	paths = []
	try:
		if a8 <= 5:
			x = 4+x
			paths.append(1)
		else:
			x = 0*x
			a8 = 8-5
			j7 = x*0
			paths.append(2)
		if j7 <= 7:
			x = x/5
			paths.append(3)
		else:
			a8 = a8*0
			a8 = 1-a8
			a8 = a8*7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))