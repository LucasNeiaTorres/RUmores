# Como rodar
1) **Crie o ambiente virtual**:
   ```sh
   python3 -m venv venv
   ```
2) **Ative o ambiente virtual**:
    - No Windows:
      ```sh
      venv\Scripts\activate
      ```
    - No Linux/Mac:
      ```sh
      source venv/bin/activate
      ```

3) **Instale as dependências**:
    ```sh
    pip install -r requirements.txt
    ```

4) **Para executar**:
    ```sh
    uvicorn main:app --reload`
    ```

# Como acessar a API
Acesse [http://localhost:8000/docs](http://localhost:8000/docs)
