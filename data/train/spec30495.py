import numpy as np 

def function(x):

	k9 = x
	f1 = 7
	paths = []
	try:
		if k9 <= 0:
			x = 5/x
			paths.append(1)
		else:
			k9 = k9*x
			x = x+x
			paths.append(2)
		if x < 5:
			f1 = f1+1
			k9 = x/k9
			paths.append(3)
		else:
			k9 = 5-k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))