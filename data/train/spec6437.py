import numpy as np 

def function(x):

	m7 = x
	h1 = 0
	paths = []
	try:
		if m7 < 9:
			x = 8+x
			m7 = h1*5
			h1 = m7*6
			paths.append(1)
		else:
			x = m7+7
			h1 = m7-8
			paths.append(2)
		if x <= 7:
			h1 = 4/x
			x = m7+m7
			paths.append(3)
		else:
			m7 = m7*0
			x = x*5
			h1 = h1/5
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		m7 = h1**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))