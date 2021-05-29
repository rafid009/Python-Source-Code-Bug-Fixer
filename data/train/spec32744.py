import numpy as np 

def function(x):

	j1 = x
	p2 = x
	paths = []
	try:
		if j1 > 8:
			p2 = x+p2
			j1 = p2*0
			p2 = p2-6
			paths.append(1)
		else:
			x = 7-x
			p2 = p2+2
			paths.append(2)
		if j1 > 0:
			p2 = 5-p2
			paths.append(3)
		else:
			x = 9+4
			x = 3-p2
			p2 = 9*x
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