import numpy as np 

def function(x):

	j7 = 8
	i5 = x
	paths = []
	try:
		if i5 <= 9:
			j7 = x/j7
			x = x-j7
			j7 = 1+j7
			paths.append(1)
		else:
			x = x+j7
			i5 = i5+7
			j7 = j7+i5
			paths.append(2)
		if j7 < 6:
			x = x*x
			j7 = j7-8
			paths.append(3)
		else:
			i5 = i5*7
			j7 = 1/j7
			j7 = j7*i5
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))