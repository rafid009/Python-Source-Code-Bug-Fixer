import numpy as np 

def function(x):

	l3 = 3
	j1 = 4
	paths = []
	try:
		if x > 2:
			j1 = x/j1
			paths.append(1)
		else:
			l3 = l3*0
			x = x+3
			paths.append(2)
		if x <= 1:
			l3 = l3*3
			paths.append(3)
		else:
			j1 = x-j1
			j1 = j1+2
			l3 = x-5
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		l3 = j1**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))