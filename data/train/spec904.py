import numpy as np 

def function(x):

	x9 = x
	p7 = x
	paths = []
	try:
		if p7 <= 4:
			p7 = 1*p7
			paths.append(1)
		else:
			x = x-p7
			x9 = 6*0
			paths.append(2)
		if x9 <= 1:
			x = x-3
			p7 = p7-x
			paths.append(3)
		else:
			x = x*2
			x = 9+x
			x9 = 1+x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		p7 = x9**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))