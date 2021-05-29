import numpy as np 

def function(x):

	j1 = x
	i7 = 9
	paths = []
	try:
		if x > 6:
			j1 = j1-1
			j1 = j1*x
			i7 = i7+0
			paths.append(1)
		else:
			j1 = j1+9
			j1 = 6+x
			paths.append(2)
		if i7 > 8:
			j1 = x/j1
			paths.append(3)
		else:
			i7 = i7-6
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))