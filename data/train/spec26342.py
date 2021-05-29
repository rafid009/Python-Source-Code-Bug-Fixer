import numpy as np 

def function(x):

	j7 = x
	p1 = x
	paths = []
	try:
		if p1 > 5:
			j7 = p1+x
			p1 = 0+p1
			paths.append(1)
		else:
			x = x/8
			p1 = 8-4
			j7 = j7/7
			paths.append(2)
		if j7 <= 2:
			j7 = 7*j7
			paths.append(3)
		else:
			x = j7*9
			x = x/4
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