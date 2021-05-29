import numpy as np 

def function(x):

	j1 = x
	p8 = 5
	x = 0
	paths = []
	try:
		if j1 > 0:
			x = 8+7
			paths.append(1)
		else:
			j1 = j1*4
			p8 = p8-p8
			paths.append(2)
		if j1 < 3:
			x = 3+0
			x = j1+3
			paths.append(3)
		else:
			j1 = j1+j1
			j1 = 8/3
			j1 = 4/7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		p8 = j1**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))