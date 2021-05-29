import numpy as np 

def function(x):

	k9 = 6
	p7 = x
	paths = []
	try:
		if k9 <= 8:
			k9 = 4+7
			k9 = 4-p7
			k9 = k9+8
			paths.append(1)
		else:
			p7 = p7-7
			p7 = 0/6
			paths.append(2)
		if p7 < 2:
			x = x+8
			p7 = p7-9
			k9 = k9*x
			paths.append(3)
		else:
			x = x+8
			p7 = p7+p7
			x = 7*1
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))