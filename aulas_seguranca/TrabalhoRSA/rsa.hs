module RSA where

import Data.Char

p  = 17 -- primos
q  = 71 -- primos
fi = (p-1) * (q-1)
n  = p * q -- 
e  = 3


-- [(0,' '), (1,'a'), (2,'b'), (3,'c'),
--  (4,'d'), (5,'e'), (6,'f'), (7,'g'),
--  (8,'h'), (9,'i'), (10,'j'),(11,'k'),
--  (12,'l'),(13,'m'),(14,'n'),(15,'o'),
--  (16,'p'),(17,'q'),(18,'r'),(19,'s'),
--  (20,'t'),(21,'u'),(22,'v'),(23,'w'),
--  (24,'x'),(25,'y'),(26,'z')]
tabelaNL = [(0,' ')] ++ [((x-96),(chr x))| x<-[97..123]]
tabelaLN = [(' ',0)] ++ [((chr x),(x-96))| x<-[97..123]]


transformarCodigo :: String -> [Int]
transformarCodigo xs 
                     | (mod (length xs) 2) == 1 = transformarCodigo' $ (xs ++ " ")
                     | otherwise = transformarCodigo' xs

transformarCodigo' :: String -> [Int]
transformarCodigo' xs = conversaoDuplas $ (foldl (\a c-> a ++ [charToCode c]) []) xs
-- helpers
transformarChar :: [Int] -> String
transformarChar xs = foldl (\z n-> z ++ [codeToChar n]) "" xs

charToCode char = snd $ head $ filter (\(l,n)->char==l) tabelaLN
codeToChar code = fst $ head $ filter (\(l,n)-> code == n ) tabelaLN

divInt :: Int -> Int -> Int
divInt a b = truncate (fromIntegral a / fromIntegral b)
--  Função Extra

conversaoDuplas :: [Int] -> [Int]
conversaoDuplas [] = []
conversaoDuplas (x:y:xs) = [ ( x * ((length tabelaLN) -1) + y ) ] ++ conversaoDuplas xs


transformarChar'' :: [Int] -> String
transformarChar'' [] = []
transformarChar'' xs = foldl (\a x -> a ++ transformarChar' x) "" xs

transformarChar' x =  codeToChar (divInt x 27) : codeToChar (mod x 27) :[]


-- rsa numeroConvertido exponencial = Int
rsa' :: Int -> Int
rsa' num = ( num ^ e ) `mod` n

rsa :: [Int] -> [Int]
rsa ns = map (rsa') ns

-- Função Codigicar String em RSA
codigicarStringToRSA  xs  = transformarChar'' $ rsa $ transformarCodigo xs








