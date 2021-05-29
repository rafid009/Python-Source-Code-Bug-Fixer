import numpy as np 

def function(x):

	g3 = x
	j1 = x
	paths = []
	try:
		if g3 > 8:
			x = 8+x
			x = x-0
			paths.append(1)
		else:
			x = j1*9
			x = x/4
			paths.append(2)
		if g3 <= 5:
			j1 = 1/j1
			x = x*2
			paths.append(3)
		else:
			j1 = j1-2
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