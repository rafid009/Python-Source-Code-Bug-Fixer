import numpy as np 

def function(x):

	p9 = x
	j9 = 1
	paths = []
	try:
		if j9 > 1:
			j9 = 0-j9
			paths.append(1)
		else:
			p9 = 0+1
			paths.append(2)
		if x >= 5:
			p9 = x-8
			x = j9+x
			p9 = 9+p9
			paths.append(3)
		else:
			j9 = 1+3
			j9 = x*j9
			x = x*x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		p9 = j9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))