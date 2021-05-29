import numpy as np 

def function(x):

	k9 = 1
	p5 = x
	paths = []
	try:
		if x >= 3:
			k9 = 5/x
			x = x/1
			paths.append(1)
		else:
			k9 = 1/1
			p5 = 5*p5
			x = x+p5
			paths.append(2)
		if x < 8:
			x = x+3
			k9 = 2+k9
			x = x-p5
			paths.append(3)
		else:
			x = x-7
			p5 = p5*1
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		x = p5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))