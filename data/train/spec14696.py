import numpy as np 

def function(x):

	j4 = x
	i5 = x
	paths = []
	try:
		if i5 > 5:
			i5 = i5*0
			j4 = 8*x
			x = 0/2
			paths.append(1)
		else:
			x = x/4
			i5 = i5/9
			j4 = 5*j4
			paths.append(2)
		if i5 > 0:
			i5 = x*i5
			paths.append(3)
		else:
			j4 = j4*j4
			j4 = 4-i5
			i5 = i5-i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))