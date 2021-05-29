import numpy as np 

def function(x):

	p3 = 4
	j7 = 7
	paths = []
	try:
		if j7 >= 5:
			j7 = j7/p3
			p3 = 7-p3
			j7 = 0+1
			paths.append(1)
		else:
			j7 = x/1
			j7 = j7-j7
			x = p3*j7
			paths.append(2)
		if p3 > 8:
			p3 = j7/7
			p3 = p3*j7
			p3 = 7/x
			paths.append(3)
		else:
			j7 = 9-j7
			p3 = x/p3
			x = x+7
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))