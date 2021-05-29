import numpy as np 

def function(x):

	j7 = 6
	p6 = x
	x = 1
	paths = []
	try:
		if p6 <= 4:
			x = 4/x
			p6 = 9+6
			x = 6+8
			paths.append(1)
		else:
			p6 = 1-p6
			j7 = 2-j7
			paths.append(2)
		if x <= 0:
			j7 = j7/1
			j7 = j7/5
			x = x-5
			paths.append(3)
		else:
			j7 = j7-x
			x = 1+x
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		j7 = p6**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))