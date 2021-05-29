import numpy as np 

def function(x):

	f3 = 4
	z9 = x
	paths = []
	try:
		if z9 < 1:
			x = 7+7
			paths.append(1)
		else:
			x = x*4
			z9 = z9+0
			z9 = x*4
			paths.append(2)
		if f3 <= 4:
			f3 = x*z9
			f3 = 3+5
			paths.append(3)
		else:
			f3 = f3+2
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		f3 = z9**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))