import numpy as np 

def function(x):

	i5 = 7
	a6 = x
	paths = []
	try:
		if a6 < 5:
			i5 = 3+a6
			i5 = i5*1
			paths.append(1)
		else:
			a6 = 0-0
			i5 = 4-a6
			i5 = 4-i5
			paths.append(2)
		if i5 <= 3:
			a6 = a6*0
			x = x+x
			paths.append(3)
		else:
			a6 = a6/i5
			a6 = 6*a6
			i5 = i5*x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))