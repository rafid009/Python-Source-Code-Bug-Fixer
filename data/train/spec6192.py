import numpy as np 

def function(x):

	r6 = x
	p3 = x
	paths = []
	try:
		if p3 > 4:
			p3 = x/3
			x = p3+1
			paths.append(1)
		else:
			x = r6/4
			x = 9+r6
			r6 = 8/r6
			paths.append(2)
		if p3 <= 5:
			r6 = r6+7
			paths.append(3)
		else:
			p3 = p3-1
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