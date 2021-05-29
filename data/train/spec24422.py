import numpy as np 

def function(x):

	p3 = 9
	k7 = 3
	paths = []
	try:
		if p3 >= 3:
			p3 = 5+p3
			x = x/6
			paths.append(1)
		else:
			p3 = x+2
			k7 = k7+7
			paths.append(2)
		if k7 <= 4:
			p3 = p3+5
			k7 = k7*x
			p3 = 3-p3
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))