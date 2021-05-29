import numpy as np 

def function(x):

	f6 = 1
	k9 = x
	paths = []
	try:
		if x <= 1:
			f6 = x+k9
			f6 = 5*f6
			paths.append(1)
		else:
			f6 = 3*3
			k9 = f6*0
			f6 = 7*x
			paths.append(2)
		if f6 > 8:
			x = 3+x
			k9 = k9+5
			paths.append(3)
		else:
			f6 = 9+f6
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		f6 = k9**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))