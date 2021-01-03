const authRequest = {
  methods: {
    /**
     * authRequest
     * 
     * Mixin-метод для более удобного взаимодействия
     * с api для представлений авторизации.
     * 
     * При неудаче выкидывает exception.
     * 
     * @param {String} url адрес, по которому нужно
     *  делать запрос
     * @param {Object} data данные, которые нужно 
     * передать с запросом
     * 
     * @returns {Object} ответ с сервера
     * @throws {Error} ошибка при неудаче
     */
    async authRequest (url, data) {
      const DEFAULT_HEADERS = { 'Content-type': 'application/json' }
      const BASE_URL = 'http://localhost:8080'
      
      const __url = `${BASE_URL}/${url}/`

      const response = await this.axios({
        method: 'POST',
        url: __url, 
        data: data,
        headers: DEFAULT_HEADERS
      })

      if (response.status !== 200 && response.status !== 201) {
        throw new Error(response.error)
      }

      return response.data
    }
  }
}

export default authRequest
