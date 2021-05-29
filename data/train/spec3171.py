import numpy as np 

def function(x):

	j7 = x
	p1 = 3
	paths = []
	try:
		if p1 > 9:
			x = j7*x
			paths.append(1)
		else:
			p1 = p1+p1
			paths.append(2)
		if j7 > 8:
			x = x+1
			paths.append(3)
		else:
			j7 = j7+x
			x = 1+4
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