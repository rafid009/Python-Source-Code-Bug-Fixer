import numpy as np 

def function(x):

	b9 = 6
	i7 = 2
	paths = []
	try:
		if b9 <= 2:
			i7 = 5*i7
			paths.append(1)
		else:
			x = 7-8
			b9 = b9*2
			b9 = x/b9
			paths.append(2)
		if i7 > 4:
			b9 = b9*0
			b9 = 2-b9
			i7 = 4/i7
			paths.append(3)
		else:
			b9 = b9+2
			i7 = x-1
			i7 = i7*2
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		b9 = i7**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))